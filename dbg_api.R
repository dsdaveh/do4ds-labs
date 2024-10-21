xx <- list(
    species = "Chinstrap",
    bill_length_mm = 39.1,
    sex = 'Male'
)

xx_prep <- list(
    bill_length_mm = xx$bill_length,
    species_Chinstrap = xx$species == "Chinstrap",
    species_Gentoo = xx$species == "Gentoo",
    sex_male = xx$sex == "Male"
)

api_url <- "http://127.0.0.1:8080/predict"

httr2::request(api_url) |>
    httr2::req_body_json(xx_prep) |>
    httr2::req_perform() |>
    httr2::resp_body_json()

