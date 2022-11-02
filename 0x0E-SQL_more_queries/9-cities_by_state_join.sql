-- Lists all cities contained in the database hbtn_0d_usa.
SELECT cy.`id`, cy.`name`, st.`name`
  FROM `cities` AS cy
       INNER JOIN `states` AS st
       ON cy.`state_id` = st.`id`
 ORDER BY cy.`id`;
