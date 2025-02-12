/* Check that the table doesn't already exist in the database. If it does,remove it from the database */
DROP TABLE IF EXISTS exercise_table;
/* Create the table in the database & give it a name */
CREATE TABLE exercise_table (
/* Tell the database which data to import, what its name in the database should be, & the type of data to import */
        exercise_name text,
        description_URL text,
        exercise_image_URL text,
        exercise_image2_URL text,
        muscle_URL text,
        muscle_group text,
        equipment_URL text,
        equipment text
);
