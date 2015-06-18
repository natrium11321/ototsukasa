SELECT
  t.id
  ,t.pos_id
  ,lat
  ,lng
  ,name
  ,sex
  ,comment
  ,rev.updatetime AS reviewedtime
  ,CASE
    WHEN empty = 'Occupied' THEN 'Occupied' WHEN
      empty = 'Empty' AND  TIMEDIFF(CURRENT_TIMESTAMP,reservedtime) < '00:10:00'
      THEN 'Reserved'
    ELSE 'Empty'
   END AS toilet_status
FROM
  toilets AS t
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
LEFT JOIN
  location AS l
ON
  t.pos_id = l.pos_id
LEFT JOIN
  (
    SELECT
      *
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
  ) AS rev
ON
  t.pos_id = rev.pos_id
