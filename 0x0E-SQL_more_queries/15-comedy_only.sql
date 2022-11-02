-- Lists all comedy shows in the database hbtn_0d_tvshows.
SELECT tv.`title`
  FROM `tv_shows` AS tv
       INNER JOIN `tv_show_genres` AS st
       ON tv.`id` = st.`show_id`

       INNER JOIN `tv_genres` AS gr
       ON gr.`id` = st.`genre_id`
       WHERE gr.`name` = "Comedy"
 ORDER BY tv.`title`;
