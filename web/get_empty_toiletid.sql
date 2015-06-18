SELECT
  toilet_id
FROM
  (
  SELECT
    t.id AS toilet_id
    ,pos_id
    ,CASE WHEN empty = 'Occupied' THEN 'Occupied' WHEN empty = 'Empty' AND  TIMEDIFF(CURRENT_TIMESTAMP,reservedtime) < '00:10:00' THEN 'Reserved' ELSE 'Empty' END AS toilet_status
  FROM
    (
      SELECT
        *
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
WHERE
  toilet_status = 'Empty' AND
  pos_id =
