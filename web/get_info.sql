SELECT
  *
FROM
  (
    SELECT
      id
      ,pos_lat
      ,pos_lng
    FROM
      toilet
  ) t
LEFT JOIN
  (
    SELECT
      id
      ,use_status
    FROM
      toilet_status
      AS a
    WHERE
      updatedt = (
        SELECT
          MAX(updatedt)
        FROM
          toilet_status
          AS b
        WHERE
          a.id = b.id
      )
  ) s
ON
  t.id = s.id
;
