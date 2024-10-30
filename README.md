# HK Store

[My Website](https://hassankh17.pythonanywhere.com/)

HK Store is a specialized e-commerce platform for cricket goods, designed to offer users an easy browsing and checkout experience. Admins have access to a dedicated interface for adding, updating, and managing products to maintain a seamless online experience for cricket enthusiasts.

## User Path
For a complete walkthrough of the user experience, please refer to the [video demonstration](#).

## Design
- **Modern Aesthetic**: Clean, contemporary design with a color scheme that adheres to WCGA AA standards.
![image](https://github.com/user-attachments/assets/2c8921e6-db0e-48c8-8efd-c2638bee4192)



- **Navigation & Icon Placement**: Key navigation elements are placed at the top, ensuring immediate visibility and intuitive access for users.
![image](https://github.com/user-attachments/assets/953c342e-9798-4a53-9490-a11bac78fc08)


- **Dynamic Banner**: The marquee banner draws attention and adds a dynamic visual.
![image](https://github.com/user-attachments/assets/59307065-e473-4002-b3a6-8a38934122ce)
![image](https://github.com/user-attachments/assets/9f7d1011-13b0-42f4-99dd-2c764848e278)
  


- **Product Cards**: Essential product details, hover effects, and a responsive design for a cohesive look.
![image](https://github.com/user-attachments/assets/81bbf83f-53a6-4abc-8cc6-6f6553d524c4)


### Interactivity
- **Stock Button Colors**: Button colors vary based on stock level, with interactive transitions.
![image](https://github.com/user-attachments/assets/455daf78-1e61-4143-a19e-9a4b2b5cf8a4)


- **Forms**: Login and registration forms are designed for simplicity, with a clean aesthetic.
![image](https://github.com/user-attachments/assets/80a919ce-a6bc-4aae-b715-d63d610a18bf)


- **Cart Management**: Plus and minus buttons for managing cart quantities, with a confirmation dialog for actions.
  ![Cart Management](images/cart_management.png) ![image](https://github.com/user-attachments/assets/631678fa-4c19-4e4e-8a67-c06ab37f4965)


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

