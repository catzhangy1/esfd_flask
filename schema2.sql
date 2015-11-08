DROP TABLE if EXISTS jetblue_data;
DROP TABLE if EXISTS contact_list;

CREATE TABLE jetblue_data (
  origin text,
  destination text,
  hotel_property text,
  hotel_nights decimal,
  hotel_check_in_date date,
  hotel_check_out_date date,
  expedia_price money,
  jetblue_price money,
  percent_savings decimal,
  month_of_travel decimal,
  advance_weeks int
);

CREATE TABLE contact_list (
  email text,
  phone text,
  hash_of_orig_dest text
);