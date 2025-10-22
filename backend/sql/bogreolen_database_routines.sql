DELIMITER ;;
CREATE PROCEDURE `AddBook`(
    IN p_Title VARCHAR(30),
    IN p_AuthorID INT, 
    IN p_Image VARCHAR(30), 
    IN p_Summary VARCHAR(200), 
    IN p_Year INT, 
    IN p_CategoryID INT
)
BEGIN
	DECLARE existing_id INT;
	SELECT bookid INTO existing_id
    FROM bookstb
    WHERE title = p_Title AND authorid = p_AuthorId
    LIMIT 1;
    
    IF existing_id IS NOT NULL THEN
		SELECT -1 AS bookid;
	ELSE
		INSERT INTO bookstb (title, authorid, image, summary, year, categoryid)
		VALUES (p_Title, p_AuthorID, p_Image, p_Summary, p_Year, p_CategoryID);
        
        SELECT LAST_INSERT_ID() AS bookid;
	END IF;
END ;;

CREATE PROCEDURE `GetBookById`(
	  IN p_BookID INT
)
BEGIN
	SELECT * FROM bookstb WHERE bookid = p_BookID;
END ;;

CREATE PROCEDURE `GetAllBooks`()
BEGIN
	SELECT * FROM bookstb;
END ;;

CREATE PROCEDURE `UpdateBook`(
	IN p_BookID INT,
    IN p_Title VARCHAR(30),
    IN p_AuthorID INT, 
    IN p_Image VARCHAR(30), 
    IN p_Summary VARCHAR(200), 
    IN p_Year INT, 
    IN p_CategoryID INT
)
proc:BEGIN
	DECLARE existing_id INT;
    DECLARE duplicate_id INT;
    
	SELECT bookid INTO existing_id
    FROM bookstb
    WHERE bookid = p_BookID
    LIMIT 1;
    
	SELECT bookid INTO duplicate_id
    FROM bookstb
    WHERE title = p_Title
    AND authorid = p_AuthorId
    AND bookid <> p_BookID
    LIMIT 1;
    
    IF duplicate_id IS NOT NULL THEN
		SELECT -2 AS Result;
        LEAVE proc;
	END IF;
    
    IF existing_id IS NULL THEN
        SELECT -1 AS Result;
        LEAVE proc;
    END IF;
    
	UPDATE bookstb
	SET title = p_Title, authorid = p_AuthorID, image = p_Image, summary = p_Summary, year = p_Year, categoryid = p_CategoryID
	WHERE bookid = p_BookID;
	
	SELECT 1 AS Result;
END ;;

DELIMITER ;