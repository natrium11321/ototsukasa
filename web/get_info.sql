SELECT
  t.toilet_id
  ,pos_lat
  ,pos_lng
  ,use_status
FROM
  (
    SELECT
      toilet_id
      ,pos_lat
      ,pos_lng
    FROM
      toilet
  ) t
LEFT JOIN
  (
    SELECT
      toilet_id
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
          a.toilet_id = b.toilet_id
      )
  ) s
ON
  t.toilet_id = s.toilet_id
;
