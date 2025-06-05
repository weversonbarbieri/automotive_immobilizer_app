-- This is the main table with all makes before manipulating the data 
create table year_make_model_table(
  id SERIAL primary key,
  year varchar(10),
  make varchar(100),
  model varchar(100),
  security text,
  parameter_reset text,
  created_at timestamp default current_timestamp,
  updated_at timestamp default current_timestamp
)

-- This is the table containing all Chevrolet brands and the hdw part numbers 
create table chevrolet_brands_hdw_table(
  id SERIAL primary key,
  year varchar(10),
  make varchar(100),
  model varchar(100),
  security text,
  hardware_part_number text,
  created_at timestamp default current_timestamp,
  updated_at timestamp default current_timestamp
)

-- Ford table
create table ford_table(
  id SERIAL primary key,
  year varchar(10),
  make varchar(100),
  model varchar(100),
  parameter_reset text,
  pats_type text,
  pats_module_location text,
  created_at timestamp default current_timestamp,
  updated_at timestamp default current_timestamp
)

-- Mercury table
create table mercury_table(
  id SERIAL primary key,
  year varchar(10),
  make varchar(100),
  model varchar(100),
  parameter_reset text,
  pats_type text,
  pats_module_location text,
  created_at timestamp default current_timestamp,
  updated_at timestamp default current_timestamp
)

-- Chevrolet table
create table chevrolet_table(
  id SERIAL primary key,
  year varchar(10),
  make varchar(100),
  model varchar(100),
  security text,
  hdw_pn text,
  is_this_hdw_clonable text,
  created_at timestamp default current_timestamp,
  updated_at timestamp default current_timestamp
)

-- Cadillac table
create table cadillac_table(
  id SERIAL primary key,
  year varchar(10),
  make varchar(100),
  model varchar(100),
  security text,
  hdw_pn text,
  is_this_hdw_clonable text,
  created_at timestamp default current_timestamp,
  updated_at timestamp default current_timestamp
)

-- Buick table
create table buick_table(
  id SERIAL primary key,
  year varchar(10),
  make varchar(100),
  model varchar(100),
  security text,
  hdw_pn text,
  is_this_hdw_clonable text,
  created_at timestamp default current_timestamp,
  updated_at timestamp default current_timestamp
)

-- Oldsmobile table
create table oldsmobile_table(
  id SERIAL primary key,
  year varchar(10),
  make varchar(100),
  model varchar(100),
  security text,
  hdw_pn text,
  is_this_hdw_clonable text,
  created_at timestamp default current_timestamp,
  updated_at timestamp default current_timestamp
)

-- GMC table
create table gmc_table(
  id SERIAL primary key,
  year varchar(10),
  make varchar(100),
  model varchar(100),
  security text,
  hdw_pn text,
  is_this_hdw_clonable text,
  created_at timestamp default current_timestamp,
  updated_at timestamp default current_timestamp
)

-- Saturn table
create table saturn_table(
  id SERIAL primary key,
  year varchar(10),
  make varchar(100),
  model varchar(100),
  security text,
  hdw_pn text,
  is_this_hdw_clonable text,
  created_at timestamp default current_timestamp,
  updated_at timestamp default current_timestamp
)

-- Hummer table
create table hummer_table(
  id SERIAL primary key,
  year varchar(10),
  make varchar(100),
  model varchar(100),
  security text,
  hdw_pn text,
  is_this_hdw_clonable text,
  created_at timestamp default current_timestamp,
  updated_at timestamp default current_timestamp
)

-- Pontiac table
create table pontiac_table(
  id SERIAL primary key,
  year varchar(10),
  make varchar(100),
  model varchar(100),
  security text,
  hdw_pn text,
  is_this_hdw_clonable text,
  created_at timestamp default current_timestamp,
  updated_at timestamp default current_timestamp
)

-- List of clonable units from Chevrolet
create table chevrolet_clonable_table(
  id SERIAL primary key,
  ecm_hardware text,
  cloning_status text,
  created_at timestamp default current_timestamp,
  updated_at timestamp default current_timestamp
)