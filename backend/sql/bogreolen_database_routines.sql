DELIMITER ;;
CREATE DEFINER=`root`@`%` PROCEDURE `AddBook`(
    IN p_Title VARCHAR(30),
    IN p_AuthorID INT, 
    IN p_Image VARCHAR(30), 
    IN p_Summary VARCHAR(200), 
    IN p_Year INT, 
    IN p_CategoryID INT
)
BEGIN
	IF NOT EXISTS (
		SELECT 1 FROM bookstb
		WHERE title = p_Title AND authorid = p_AuthorID
    ) THEN
		INSERT IGNORE INTO bookstb (title, authorid, image, summary, year, categoryid)
		VALUES (p_Title, p_AuthorID, p_Image, p_Summary, p_Year, p_CategoryID);
        SELECT "Entry succesfully added!" as OUTPUT;
	ELSE
		SELECT "Entry already exists!" as OUTPUT;
	END IF;
END ;;
DELIMITER ;