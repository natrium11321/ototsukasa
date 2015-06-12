SELECT
  main.pos_id
  ,pos_lat
  ,pos_lng
  ,num
  ,empty_num
  ,occupied_num
  ,reserved_num
  ,comment
FROM
  (
  SELECT
    pos_id
    ,pos_lat
    ,pos_lng
    ,COUNT(*) AS num
    ,COUNT(toilet_status = 'Empty' or NULL) AS empty_num
    ,COUNT(toilet_status = 'Occupied' or NULL) AS occupied_num
    ,COUNT(toilet_status = 'Reserved' or NULL) AS reserved_num
  FROM
    (
    SELECT
      t.id
      ,pos_id
      ,pos_lat
      ,pos_lng
      ,CASE WHEN empty = 'Occupied' THEN 'Occupied' WHEN empty = 'Empty' AND  TIMEDIFF(CURRENT_TIMESTAMP,reservedtime) < '00:10:00' THEN 'Reserved' ELSE 'Empty' END AS toilet_status
    FROM
      (
        SELECT
          id
          ,pos_id
          ,pos_lat
          ,pos_lng
        FROM
          toilets
      ) t
    LEFT JOIN
      (
        SELECT
          toilet_id
          ,empty
        FROM
          status
          AS a
        WHERE
          updatetime = (
            SELECT
              MAX(updatetime)
            FROM
              status
              AS b
            WHERE
              a.toilet_id = b.toilet_id
          )
      ) s
    ON
      t.id = s.toilet_id
    LEFT JOIN
      (
        SELECT
          toilet_id
          ,updatetime AS reservedtime
        FROM
          reservations AS a
        WHERE
          updatetime = (
            SELECT
              MAX(updatetime)
            FROM
              reservations
              AS b
            WHERE
              a.toilet_id = b.toilet_id
          )
      ) r
    ON
      t.id = r.toilet_id
    ) sub
  GROUP BY
    pos_id,pos_lat,pos_lng
  ) main
LEFT JOIN
  (
    SELECT
      pos_id
      ,comment
    FROM
      reviews AS a
    WHERE
      updatetime = (
        SELECT
          MAX(updatetime)
        FROM
          reviews AS b
        WHERE
          a.pos_id = b.pos_id
      )
  ) sub
ON
  main.pos_id = sub.pos_id
;
