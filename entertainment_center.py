import fresh_tomatoes
import media


# The data that is pulled for each individual movie.

lethal_weapon = media.Movie(
    "Lethal Weapon",
    "110 minutes",
    "Unlikely cop duo brings down a drug trafficking group.",
    "Richard Donner",
    "March 6th 1987",
    "https://upload.wikimedia.org/wikipedia/en/d/d9/Lethal_weapon1.jpg",
    "https://www.youtube.com/watch?v=bKeW-MGu-qQ")

# print (lethal_weapon.storyline)--test I ran to make sure it worked.
die_hard = media.Movie(
    "Die Hard",
    "132 minutes",
    "Everyday cop must stop terrorist in an unfamiliar city.",
    "John McTiernan",
    "July 12th 1988",
    "https://upload.wikimedia.org/wikipedia/en/7/7e/Die_hard.jpg",
    "https://www.youtube.com/watch?v=04U3IU7IDac")

indiana_jones_3 = media.Movie(
    "Indiana Jones and The Last Crusade",
    "128 mintues",
    "Archeologist must save his father and "
    "race the Nazi regime to a religous relic", #noqa
    "Steven Spielberg",
    "May 24th 1989",
    "https://upload.wikimedia.org/wikipedia/en/f/fc/Indiana_Jones_and_the_Last_Crusade_A.jpg", #noqa
    "https://www.youtube.com/watch?v=s_9hAVJUHBw")

serenity = media.Movie(
    "Serenity",
    "119 minutes",
    "A space captain and his crew risk their "
    "lives in the search for the truth.",
    "Joss Whedon",
    "August 22nd 2005",
    "https://upload.wikimedia.org/wikipedia/en/9/9e/Serenity_One_Sheet.jpg",
    "https://www.youtube.com/watch?v=JY3u7bB7dZk")

grandmas_boy = media.Movie(
    "Grandma's Boy",
    "94 minutes",
    "A game tester must move in with his grandmother "
    "and learn to adapt his lifestyle",
    "Nicholaud Goosen",
    "January 6th 2006",
    "https://upload.wikimedia.org/wikipedia/en/2/26/Grandma%27s_Boy_poster.jpg", #noqa
    "https://www.youtube.com/watch?v=u_WFNJEJs8U")

back_to_the_future = media.Movie(
    "Back To The Future",
    "116 minutes",
    "Teenage boy finds out how complicated time travel can be",
    "Robert Zemeckis",
    "July 3rd 1985",
    "https://upload.wikimedia.org/wikipedia/en/d/d2/Back_to_the_Future.jpg",
    "https://www.youtube.com/watch?v=qvsgGtivCgs")

# The list of the movies to be pulled into the html/css
# webpage format provided.

movies =[lethal_weapon, die_hard, indiana_jones_3,
        serenity, grandmas_boy, back_to_the_future]
fresh_tomatoes.open_movies_page(movies)
