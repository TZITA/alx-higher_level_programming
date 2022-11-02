-- Lists all shows without the comedy genre in the database hbtn_0d_tvshows.
SELECT DISTINCT `title`
  FROM `tv_shows` AS tv
       LEFT JOIN `tv_show_genres` AS st
       ON st.`show_id` = tv.`id`

       LEFT JOIN `tv_genres` AS gr
       ON gr.`id` = st.`genre_id`
       WHERE tv.`title` NOT IN
             (SELECT `title`
                FROM `tv_shows` AS tv
	             INNER JOIN `tv_show_genres` AS st
		     ON st.`show_id` = tv.`id`

		     INNER JOIN `tv_genres` AS gr
		     ON gr.`id` = st.`genre_id`
		     WHERE gr.`name` = "Comedy")
 ORDER BY `title`;
