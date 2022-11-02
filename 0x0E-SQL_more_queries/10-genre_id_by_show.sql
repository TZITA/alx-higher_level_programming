-- Lists all shows contained in hbtn_0d_tvshows that have at least one genre.
SELECT st.`title`, gr.`genre_id`
  FROM `tv_shows` AS st
        INNER JOIN `tv_show_genres` AS gr
	ON st.`id` = gr.`show_id`
 ORDER BY st.`title`, gr.`genre_id`;
