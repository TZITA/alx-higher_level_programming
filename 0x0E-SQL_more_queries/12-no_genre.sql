-- Lists all shows in the database hbtn_0d_tvshows without a genre linked.
SELECT st.`title`, gr.`genre_id`
  FROM `tv_shows` AS st
       LEFT JOIN `tv_show_genres` AS gr
       ON st.`id` = gr.`show_id`
       WHERE gr.`genre_id` IS NULL
 ORDER BY st.`title`, gr.`genre_id`;
