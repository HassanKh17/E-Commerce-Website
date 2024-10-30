# My Website
HK Store is an e-commerce platform specialised in cricket goods, enabling users to easily browse and checkout. Admins have an interface to effortlessly add, update, and manage cricket products, ensuring a seamless online experience for cricket enthusiasts.

## User Path
[Watch the User Flow Video](https://leeds365-my.sharepoint.com/:v:/g/personal/sc22hkar_leeds_ac_uk/EVsQlcKRkz9JsCGJqc-T_ZcBXtW__B_MjdXJxHaMHg8VFw?e=ob2KAz)

## Design
The website boasts a contemporary aesthetic with a clean and modern design. The colour scheme, featuring `#f5f5f5` for the background and `#333` for the navigation bar has a contrast ratio of approximately 4.49:1, meeting the WCGA AA standards for normal text.

![Navigation Bar and Color Scheme](https://github.com/user-attachments/assets/2ccfc37a-c9b6-460a-bc78-e14dbd2f0166)

The navigation bar is positioned at the top with icons in the top-right corner to optimize user experience and aesthetics. Its top placement ensures immediate visibility, adhering to conventional design patterns.

![Top Placement and Icon Positioning](https://github.com/user-attachments/assets/80fe137f-8511-4e8d-b297-fef0338a4c77)

The website includes a set of thoughtfully chosen icons, enhancing the overall aesthetics and contributing to an intuitive user interface. Each icon conveys specific actions or information, promoting a seamless and visually engaging experience.

![Icon Placement](https://github.com/user-attachments/assets/edeff686-dc86-4131-bc58-d2b5b36c0d64)

A moving banner, achieved through the `<marquee>` element, adds a dynamic and visually stimulating aspect to the page, capturing users' attention immediately.

![Moving Banner](https://github.com/user-attachments/assets/ac4753f5-1b02-490f-b77f-abfead0c995a)

### Product Cards
The product cards maintain a consistent design, contributing to a cohesive and professional look. Each card includes product details like name, image, and price for quick access to relevant information.

![Product Cards](https://github.com/user-attachments/assets/45fc2c4f-d6ca-4661-b5ed-2d8a3015d9a0)

A subtle scaling effect on hover provides visual feedback when users interact with the product cards.

![Hover Effect on Product Cards](https://github.com/user-attachments/assets/2ea65cbc-bafa-4133-840c-2679ce1743fd)

The use of flexbox in the product container allows for a responsive layout, adapting to different screen sizes.

![Responsive Layout with Flexbox](https://github.com/user-attachments/assets/1e420f3a-c50e-44bd-ac76-204b096a51af)

### Purchase Button
To enable product purchases, a button is included at the bottom of each card. The button appearance varies based on stock availability:

- **In Stock:** Solid background color of `rgb(67, 147, 151)` with a lighter shade on hover.
- **Out of Stock:** Muted background color of `#ccc` indicating its disabled state.

![Purchase Button](https://github.com/user-attachments/assets/cff09f23-0393-4cf9-b1d9-0e40790f276a)

This color choice effectively communicates button interactivity, with a `not-allowed` cursor style for disabled buttons, aligning with standard conventions.

![Disabled Button with Not-Allowed Cursor](https://github.com/user-attachments/assets/df1ede6f-9639-46d8-9fac-04ccbb47feb1)

### Forms
Login and registration forms are kept simple for ease of use, requiring only essential information.

![Login and Registration Forms](https://github.com/user-attachments/assets/7e2d6626-747c-423f-aacb-ede6ba30fc32)

The white background and rounded corners of the forms create a clean and modern appearance, while percentage-based width and margin properties ensure responsiveness.

### Profile Icon
A profile icon in the top left of each navbar displays “Guest” if the user is not logged in, and switches to the username upon login, establishing a sense of identity.

![Profile Icon Display](https://github.com/user-attachments/assets/702fb9f9-8cfa-4f47-997c-ebc6dbde85ba)

### Cart Table
Cart items are displayed in a visually cohesive table, with the table's color scheme aligned with the website’s primary colors and a black-box shadow for visual prominence.

![Cart Table](https://github.com/user-attachments/assets/e4041d6a-3f9d-43cc-b486-5160da14cf22)

Additional touches, like alternating row colors and a hover effect, further enhance readability and user experience. This same table style is used for both admin and user views.

![Table for Order History and Admin View](https://github.com/user-attachments/assets/e3bdd9f7-4858-4eac-8f23-2194e1a9460b)

### Cart Item Management
Buttons with plus and minus icons allow users to adjust quantities of items in their cart intuitively.

![Cart Quantity Management](https://github.com/user-attachments/assets/c5f4e872-c76d-4340-b4fa-3b1c0b8ac1ad)

A confirmation dialog ensures users are prompted before making changes, adding an extra layer of protection against accidental actions.

### Product Review Form
For users to review purchased products, a simple form is available in the final column of the order history table, offering a convenient way to submit reviews without navigating away.

![Review Form in Order History](https://github.com/user-attachments/assets/a0f470de-17ac-437d-8ebf-27341762d788)

### Admin Edit Form
An admin edit form appears in a modal overlay, drawing focus to editing tasks without interference from other page elements. JavaScript functions control the overlay, creating a dynamic user experience.

![Admin Edit Form](https://github.com/user-attachments/assets/027d476a-b249-4972-870e-0a535b4043da)

## Accessibility

- **Readable Fonts and Sizes:** Use of 'Roboto' font family with appropriate sizes enhances readability for all users.

![Roboto Font Usage](https://github.com/user-attachments/assets/8d92d908-66a1-49e6-b4b7-f8786e9c54cc)

- **Iconic Representation:** Recognizable icons aid navigation, particularly for users with cognitive disabilities.

![Accessible Icon Design](https://github.com/user-attachments/assets/7948ef9b-642b-43d4-8b38-00b30d834992)

- **Inclusive Image Descriptions:** Alt text accompanies images, essential for users relying on screen readers.

![Alt Text for Images](https://github.com/user-attachments/assets/5b093646-c90f-45b1-a5a3-966d46b29166)

## Database Structure
The database has five tables: `User`, `Product`, `Stock`, `Order`, `OrderItem`, and `Review`.

### Relationships

- **User and Order:** Each user can have multiple orders.
- **Product and Stock:** Each product has multiple stock entries.
- **Product and OrderItem:** Each product appears in multiple order items.
- **User and Review:** Users can write multiple reviews, each associated with a single user.
- **Product and Review:** Products can have multiple reviews.
- **OrderItem and Review:** Each order item can have multiple reviews.

![Database Relationships](https://github.com/user-attachments/assets/7360efc1-8944-41a7-b100-fdd3577d196c)

## Advanced Feature: Search and Filter
The search and filter section offers structured and intuitive features to enhance usability.

![Search and Filter Section](https://github.com/user-attachments/assets/f18b9080-6c5a-455c-982f-57c01d7a5fd5)

Users can sort listings based on their preferences, utilizing JavaScript functions for real-time updates without page reloads.

![Sorting Options](https://github.com/user-attachments/assets/181f06a6-3baa-4bd1-a3b1-1c40b5894476)

