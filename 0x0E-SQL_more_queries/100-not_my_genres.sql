-- Lists all genres of the database hbtn_0d_tvshows not linked to the show Dexter.
SELECT DISTINCT `name`
  FROM `tv_genres` AS gr
       INNER JOIN `tv_show_genres` AS st
       ON gr.`id` = st.`genre_id`

       INNER JOIN `tv_shows` AS tv
       ON st.`show_id` = t.`id`
       WHERE gr.`name` NOT IN
             (SELECT `name`
                FROM `tv_genres` AS gr
	             INNER JOIN `tv_show_genres` AS st
		     ON gr.`id` = st.`genre_id`

		     INNER JOIN `tv_shows` AS tv
		     ON st.`show_id` = tv.`id`
		     WHERE tv.`title` = "Dexter")
 ORDER BY gr.`name`;
