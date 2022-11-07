-- Lists all genres of the show Dexter in the database hbtn_0d_tvshows.

SELECT gr.`name`
  FROM `tv_genres` AS gr
       INNER JOIN `tv_show_genres` AS st
       ON gr.`id` = st.`genre_id`

       INNER JOIN `tv_shows` AS tv
       ON tv.`id` = st.`show_id`
       WHERE tv.`title` = "Dexter"
 ORDER BY gr.`name` ASC;
