CREATE DATABASE ABC_Computer;
USE ABC_Computer;
CREATE TABLE Computer (SerialNumber INT PRIMARY KEY, Make TEXT (12), Model TEXT (24), ProcessorType TEXT (24),ProcessorSpeed FLOAT, MainMemory TEXT(15), DiskSize TEXT(15));
INSERT INTO Computer VALUES (9871234, "HP", "Pavilion 500-210qe", "Intel i5-4530", 3.00, "6.0 Gbytes", "1.0 Tbytes"),(9871235, "HP", "Pavilion 500-210qe", "Intel i5-4531", 3.00, "6.0 Gbytes", "1.0 Tbytes"),
(9871236, "HP", "Pavilion 500-210qe", "Intel i5-4532", 3.00, "6.0 Gbytes", "1.0 Tbytes"),(9871237, "HP", "Pavilion 500-210qe", "Intel i5-4533", 3.00, "6.0 Gbytes", "1.0 Tbytes"),
(9871238, "HP", "Pavilion 500-210qe", "Intel i5-4534", 3.00, "6.0 Gbytes", "1.0 Tbytes"),(9871239, "HP", "Pavilion 500-210qe", "Intel i5-4535", 3.00, "6.0 Gbytes", "1.0 Tbytes");

ALTER TABLE Computer ADD Graphics TEXT(40)NOT NULL COMMENT "Must be all 'Integrated Intel HD Graphics 4600'";

ALTER TABLE Computer DROP COLUMN ProcessorSpeed;

UPDATE Computer SET Graphics = 'Integrated Intel HD Graphics 4600' WHERE SerialNumber = 2;
UPDATE Computer SET Graphics = 'Integrated Intel HD Graphics 4600' WHERE SerialNumber = 3;
UPDATE Computer SET Graphics = 'Integrated Intel HD Graphics 4600' WHERE SerialNumber = 4;

SELECT*FROM Computer;
SELECT*FROM Computer WHERE Make = "HP";