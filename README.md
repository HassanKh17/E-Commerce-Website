# HK Store

[My Website](https://hassankh17.pythonanywhere.com/)

HK Store is a specialized e-commerce platform for cricket goods, designed to offer users an easy browsing and checkout experience. Admins have access to a dedicated interface for adding, updating, and managing products to maintain a seamless online experience for cricket enthusiasts.

## User Path
For a complete walkthrough of the user experience, please refer to the [video demonstration](#).

## Design
- **Modern Aesthetic**: Clean, contemporary design with a color scheme that adheres to WCGA AA standards.
  ![Homepage Design](images/homepage_design.png)

- **Navigation & Icon Placement**: Key navigation elements are placed at the top, ensuring immediate visibility and intuitive access for users.
  ![Navigation Bar](images/navigation_bar.png)

- **Dynamic Banner**: The marquee banner draws attention and adds a dynamic visual.
  ![Dynamic Banner](images/dynamic_banner.png)

- **Product Cards**: Essential product details, hover effects, and a responsive design for a cohesive look.
  ![Product Cards](images/product_cards.png)

### Interactivity
- **Stock Button Colors**: Button colors vary based on stock level, with interactive transitions.
  ![Stock Buttons](images/stock_buttons.png)

- **Forms**: Login and registration forms are designed for simplicity, with a clean aesthetic.
  ![Login Form](images/login_form.png)

- **Cart Management**: Plus and minus buttons for managing cart quantities, with a confirmation dialog for actions.
  ![Cart Management](images/cart_management.png)

## Accessibility
- **Readable Fonts**: 'Roboto' font ensures clarity, with appropriately sized text.
- **Iconic Representation**: Recognizable icons enhance the interface, aiding users with cognitive disabilities.
- **Inclusive Design**: Alt text for images, overlay flash messages, and intuitive navigation elements contribute to an accessible experience.

## Database Structure
The database includes tables for `User`, `Product`, `Stock`, `Order`, `OrderItem`, and `Review`, with the following many-to-many relationships:
- **User & Order**: Each user can have multiple orders.
- **Product & Stock**: Each product can have multiple stock entries.
- **User & Review**: Each user can leave multiple reviews for products they’ve purchased.
  
## Advanced Feature: Search & Filter
- **Search Bar**: Allows users to find products quickly by typing keywords.
  ![Search Bar](images/search_bar.png)

- **Category Filter**: Dropdown menu for narrowing down product categories.
  ![Category Filter](images/category_filter.png)

- **Sorting Options**: Buttons for price sorting, providing a personalized product listing experience.
  ![Sorting Options](images/sorting_options.png)

- **Real-Time Updates**: JavaScript functions for dynamic filtering and sorting.

## Testing & Critical Analysis
### What Went Well
- Effective real-time updates and feedback mechanisms.
- AJAX requests for sorting and searching, improving the dynamic user experience.

### Challenges
- Responsive design for different screens posed challenges due to the initial lack of a mobile-first approach.

### Improvements
- **Accessibility**: Conduct a thorough audit to ensure WCAG compliance.
- **Recommendation System**: A future feature to recommend products based on user preferences and history.

## Bibliography
All images sourced from [Allrounder Cricket](https://www.allroundercricket.com/).
