-- Demostración del CRUD directamente en MySQL/MariaDB (para la defensa).
-- Ejecutar en phpMyAdmin (pestaña SQL) con la base inmobiliaria_db seleccionada,
-- DESPUÉS de correr "python manage.py migrate".

-- CREATE
INSERT INTO propiedad
 (titulo, tipo, operacion, direccion, ciudad, precio, habitaciones, banos, area_m2,
  anio_construccion, estado, descripcion, contacto_nombre, contacto_correo, fecha_registro)
VALUES
 ('Casa de prueba SQL', 'CASA', 'VENTA', 'Calle Falsa 123', 'Santiago', 120000000.00, 3, 2, 140.00,
  2010, 'DISPONIBLE', 'Insertada desde SQL', 'Demo', 'demo@correo.cl', NOW());

-- READ
SELECT id, titulo, ciudad, precio, estado FROM propiedad ORDER BY id DESC;

-- UPDATE
UPDATE propiedad SET precio = 125000000.00, estado = 'RESERVADA'
WHERE titulo = 'Casa de prueba SQL';

-- DELETE
DELETE FROM propiedad WHERE titulo = 'Casa de prueba SQL';
