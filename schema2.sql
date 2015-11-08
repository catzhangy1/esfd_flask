DROP TABLE if EXISTS jetblue_data;
DROP TABLE if EXISTS contact_list;

CREATE TABLE jetblue_data (
  origin text,
  destination text,
  hotel_property text,
  hotel_nights decimal,
  hotel_check_in_date text,
  hotel_check_out_date text,
  expedia_price decimal,
  jetblue_price decimal,
  percent_savings decimal,
  month_of_travel decimal,
  advance_weeks int
);

CREATE TABLE contact_list (
  name text,
  email text,
  origin text,
  destination text,
  hotel_nights decimal,
  hotel_check_in_date text,
  tolerance int,
  max_price decimal
);