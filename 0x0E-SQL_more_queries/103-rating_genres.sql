-- Lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT `name`, SUM(`rate`) AS `rating`
  FROM `tv_genres` AS gr
       INNER JOIN `tv_show_genres` AS st
       ON st.`genre_id` = gr.`id`

       INNER JOIN `tv_show_ratings` AS r
       ON r.`show_id` = st.`show_id`
 GROUP BY `name`
 ORDER BY `rating` DESC;
