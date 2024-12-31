SELECT 
    product_id, 
    product_name
FROM 
    product
WHERE 
    is_recyclable = TRUE 
    AND is_low_fat = TRUE;