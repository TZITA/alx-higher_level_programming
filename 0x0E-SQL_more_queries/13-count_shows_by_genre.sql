-- Lists all genres from the database hbtn_0d_tvshows along with the number of shows linked to each.
SELECT gr.`name` AS `genre`,
       COUNT(*) AS `number_of_shows`
  FROM `tv_genres` AS gr
       INNER JOIN `tv_show_genres` AS tv
       ON gr.`id` = tv.`genre_id`
 GROUP BY gr.`name`
 ORDER BY `number_of_shows` DESC;
