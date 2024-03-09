CREATE TABLE IF NOT EXISTS property_details
(
    id serial NOT NULL,
    url text,
    price numeric,
    square_footage numeric,
    building_ownership text,
    number_of_rooms integer,
    construction_status text,
    floor text,
    rent numeric,
    parking text,
    heating text,
    city text,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    price_currency text,
    rent_currency text,
    CONSTRAINT property_details_pkey PRIMARY KEY (id)
);