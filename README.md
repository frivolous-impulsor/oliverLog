# projTree by Oliver Li, visit the web at https://frivolousimpulsor95.pythonanywhere.com/
The website is a django project that supports user login/out/register. Upon logged in, a user is entitled to create/edit/delete abtrary number of seed profiles of theirs.
A seed profile is a basic introduction of a seed, including it's name, time to obtain(month of the year), growth rate, picture, picture after grow up, general difficulty to plant, and maybe more. Each seed possesses numerous steps to plant, including how to extract seed, process seed, plant seed, after plant measurements, watering frequency and all based on user's understanding and preference.
A visitor, regardless of log status, is able to check the list of seed types based on their attributes like obtain month, growth rate, difficulty to plant, and maybe more.

Backend:
As the project grows, it's additional functionality weighs visibly heavier than it's initial prototype "post", which is the skelliton I've followed from Corey Shafer's Django beginer course at Youtube. And accordingly, it leans ever more towards my initial incentive of learning django, which is to build a website that utilize backend database to analytically deliver informtaion about planting techniques, for fruit seeds like lemon, apple, and tree seeds like acorn and whatever that I haven't heard of. Surprisingly, with the robust class views and models of django, I can easily build an interactive website that receives user input and store them in database.

Front end
The website is styled using bootstrap5. Thanks to its convenience, a couple keywords can make this website at least not aesthetically repelling.
I'm considering between Vue or React for javascript framework. Honestly, I don't even know javascript yet, and the website at current state doesn't appear to need any javascript. So it's currently not equiped with any front-end framework except bootstrap5.
