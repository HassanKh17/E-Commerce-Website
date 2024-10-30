# My Website
HK Store is an e-commerce platform specialised in cricket goods, enabling users to easily browse and checkout. Admins have an interface to effortlessly add, update, and manage cricket products, ensuring a seamless online experience for cricket enthusiasts.

## User Path
https://leeds365-my.sharepoint.com/:v:/g/personal/sc22hkar_leeds_ac_uk/EVsQlcKRkz9JsCGJqc-T_ZcBXtW__B_MjdXJxHaMHg8VFw?e=ob2KAz

## Design
The website boasts a contemporary aesthetic with a clean and modern design. The colour scheme, featuring `#f5f5f5` for the background and `#333` for the navigation bar has a contrast ratio of approximately 4.49:1 which meets the WCGA AA standards for normal text.

The placement of the navigation bar at the top and the positioning of icons in the top right corner have been carefully considered to optimize user experience and aesthetics.
The top placement of the navbar ensures immediate visibility, drawing user attention to essential navigation elements. It also adheres to conventional design patterns, making it intuitive for users accustomed to standard web layouts.

The website incorporates a set of thoughtfully chosen icons, enhancing the overall aesthetics, and contributing a more intuitive user interface. Each icon is strategically placed to convey specific actions or information, promoting a seamless and visually engaging experience for users.

The moving banner, achieved through `<marquee>` element, attracts immediate attention and adds a dynamic element to the web page. It enhances the visual appeal, providing users with a visually stimulating element.

The product cards maintain a consistent design, contributing to cohesive and professional look for the website. Each card includes essential details like product name, image, and price, ensuring users have quick access to relevant information.

The subtle scaling effect on hover adds an interactive dimension, providing visual feedback to users when interacting with product cards.
The use of flex box in the product container allows for a responsive layout, adapting to different screen sizes. Similar product containers are applied on the product page with slight modifications.

As now we want the user to be able to buy a product, a button is added at the bottom of the card. The button would vary depending on the stock level of the product.
If the product is in stock, the button has a solid background colour of `rgb(67, 147, 151)` as it aligns with the overall colour scheme of the website.
The button transitions to a slightly lighter shade on hover; this crafty change adds a dynamic and interactive feel to the button.
If the product is out of stock, the button has a muted background colour of `#ccc` indicating its disabled state.
The colour choice effectively communicates that the button is inactive. The cursor style `not-allowed` visually presents that the button is not interactive. This is a standard convention for disabled elements on most websites.

Both the forms for login and registration are kept quite simple and straightforward for the ease of the user. They only require the user to input essential details that would be required to login or register.
The choice of white background for the form creates a clean and modern appearance, providing a neutral canvas for other elements.
The form’s rounded corners soften its edges, contributing to a more inviting and user-friendly aesthetic. The form incorporates user-friendly elements like clear labels for input fields, which contribute to an accessible design.
To keep the forms responsive, percentage-based width and margin properties are used.

In the top left corner of each navbar, there is a profile icon with text next to it. If the user hasn’t logged in, it displays “Guest”. When a user logs in, it is replaced by the username of the user. This lets the user know if they have logged in or not and establishes a sense of identity and acknowledgement.

The cart items are displayed in a table with the relevant fields. The colour scheme of the table is consistent with the website’s primary colours, creating a visually cohesive design. The application of black-box shadow enhances the container’s visual prominence.
The semi-transparent background of table containers adds a touch of colour while allowing the underlying content to show through. The collapse borders provide a clean and seamless look.
A solid background colour, which contrasts with the rest of the table, is applied to the header, creating a clear separation from the rest of the table.
To add more to the visual appeal of the table, alternating row colours are applied to enhance readability and add a dynamic touch.
Furthermore, to elevate the user experience, a hover effect is applied to the rows of the table. The alternating colours on hover add subtle interactive response.

The same table style has been used for admin to view existing products and for users to see their order history. This provides a uniform experience throughout the website.

To add or remove an item from the cart, two buttons with icons are present. The icons, presumably depicting minus and plus symbols, provide clear and intuitive indications of their respective actions. The button with the plus icon adds one more to the quantity of an existing item in the cart, while the button with the minus icon does the opposite. The use of icons adds a modern and stylish touch to the buttons.

When the above buttons are pressed, a confirmation dialog ensures that users are prompted before taking any action, preventing accidental clicks.
This user-friendly feature adds an extra layer of protection against unintended item removal or addition.

For the user to review the products they have purchased, a very simple form is available in the final column of the order history table. The purpose of this form is to provide a convenient way to submit reviews without navigating to a separate review page.
Clear and concise options for ratings 1 to 5 stars can be selected by using a dropdown.

A multiline text input for users to provide written reviews. A clearly labelled “Submit Review” button is there to indicate the purpose of the form.
For the admin to edit an existing product, an edit form is structured with the modal, creating a clear separation from the main content, and providing a focused area for editing.
The use of a modal overlay is to ensure that the form captures the admin’s attention while preventing interference with other elements on the page.
The use of JavaScript functions for opening and closing the overlay/modal adds a dynamic and interactive aspect to the form.
The form dynamically populates fields with existing data, allowing the admin to edit specific details of the product seamlessly.

## Accessibility

- **Readable Fonts and Sizes:** The use of the 'Roboto' font family enhances readability, and font sizes are appropriately set. Clear and legible text is crucial for users with visual impairments or those who may rely on screen readers.

- **Iconic Representation:** Icons, such as those in the navbar, are visually recognizable and enhance the user interface. This is particularly beneficial for users with cognitive disabilities who might find it easier to navigate through familiar symbols.

- **Inclusive Image Descriptions:** Images are accompanied by descriptive alt text. This is vital for users with visual impairments who rely on screen readers to understand the content of images.

- **Thoughtful Flash Message Display:** Flash messages are presented in an overlay with attention to aesthetics. The overlay design ensures that users, including those with cognitive or attention-related challenges, can focus on and comprehend important messages.

- **Intuitive Navigation:** The layout and organization of navigation elements contribute to an intuitive user experience. Clear navigation is essential for users with cognitive disabilities or those who may face challenges in understanding complex structures.

## Database
My database structure has 5 tables: `User`, `Product`, `Stock`, `Order`, `OrderItem`, and `Review`.
Following are the Many-to-Many relationships in my database:

- **User and Order:**
  - Each user can have multiple orders (`User.orders`).
  - Each order belongs to a single user (`Order.user`).

- **Product and Stock:**
  - Each product can have multiple stock entries (`Product.stock`).
  - Each stock entry is associated with a single product (`Stock.product`).

- **Product and OrderItem:**
  - Each product can be included in multiple order items (`Product.order_items`).
  - Each order item is associated with a single product (`OrderItem.product`).

- **User and Review:**
  - Each user can write multiple reviews (`User.reviews`).
  - Each review is associated with a single user (`Review.user`).

- **Product and Review:**
  - Each product can have multiple reviews (`Product.reviews`).
  - Each review is associated with a single product (`Review.product`).

- **OrderItem and Review:**
  - Each order item can have multiple reviews (`OrderItem.reviews`).
  - Each review is associated with a single order item (`Review.order_item`).

Users can view their order history, as each order is linked to a specific user. This enhances the user experience by providing a comprehensive record of their purchases.

Users can leave reviews for products they’ve purchased, contributing to a collaborative and informative shopping experience.
Stock information is tracked for each product, ensuring accurate inventory management. This provides admin with insights into stock levels.

## Advanced Feature
The layout of the search and filter section is structured and intuitive, making it easy for users to understand and interact with these advanced features.
The search bar allows users to find products quickly by typing relevant keywords. This feature enhances the overall usability of the website, particularly for users who have specific products in mind.
Placeholder text in the search bar ("Search for products") and descriptive options. This is especially helpful for those who may require additional guidance.

The category filter, presented as a dropdown menu, allows users to narrow down their search by selecting a specific product category.
This enhances the efficiency of product discovery, making it easier for users to find what they are looking for.
The select menu for choosing a category is interactive and engages users in a visually pleasing way. This feature is not only functional but also adds an aesthetic touch to the filtering process.

The sorting buttons ("Sort by Price (High to Low)" and "Sort by Price (Low to High)") provide users with a dynamic and personalized way to organize product listings based on their preferences. This feature caters to diverse user needs and preferences.

The use of JavaScript functions (`sortProducts` and `filterProductsByCategory`) indicates real-time updates and a seamless user experience without the need for page reloads. This contributes to a more interactive and modern feel.
