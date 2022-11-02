-- Lists all shows and genres linked to the show from the database hbtn_0d_tvshows.
SELECT tv.`title`, gr.`name`
  FROM `tv_shows` AS tv
       LEFT JOIN `tv_show_genres` AS st
       ON tv.`id` = st.`show_id`

       LEFT JOIN `tv_genres` AS gr
       ON st.`genre_id` = gr.`id`
 ORDER BY tv.`title`, gr.`name`;
