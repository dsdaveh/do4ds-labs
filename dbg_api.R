# Correct the xx_prep object and field access
xx <- list(
    species = "Chinstrap",
    bill_length = 39.1,
    sex = "Male"  
)

xx_prep <- list(
    bill_length_mm = xx$bill_length,
    species_Chinstrap = xx$species == "Chinstrap",
    species_Gentoo = xx$species == "Gentoo",
    sex_male = xx$sex == "Male"
)

# Define the API endpoint
api_url <- "http://127.0.0.1:8080/predict"

# Sending the request with the correct format
response <- httr2::request(api_url) |>
    httr2::req_body_json(list(xx_prep)) |>
    httr2::req_perform() |>
    httr2::resp_body_json()

# View the response
print(response)


