-- Lists all shows contained in the database hbtn_0d_tvshows.
SELECT st.`title`, gr.`genre_id`
  FROM `tv_shows` AS st
       LEFT JOIN `tv_show_genres` AS gr
       ON st.`id` = gr.`show_id`
 ORDER BY st.`title`, gr.`genre_id`;
