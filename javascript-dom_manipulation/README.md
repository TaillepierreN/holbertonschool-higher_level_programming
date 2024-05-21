```markdown
# JavaScript DOM Manipulation

## Overview

This project focuses on JavaScript DOM manipulation. The exercises involve selecting and modifying HTML elements, handling events, and fetching data from APIs. By completing this project, you will gain practical experience with JavaScript and the Document Object Model (DOM), enhancing your ability to create dynamic and interactive web applications.

## Learning Objectives

By the end of this project, you should be able to:

- Select HTML elements using JavaScript.
- Understand the differences between ID, class, and tag name selectors.
- Modify the style and content of HTML elements.
- Manipulate the DOM structure.
- Make requests with `XMLHttpRequest` and `Fetch API`.
- Listen and bind to DOM and user events.

## Requirements

- **Editors**: Any code editor of your choice.
- **Browser**: Chrome (version 57.0 or later).
- **File Endings**: All files should end with a new line.
- **Coding Standards**: Follow semistandard coding style. No usage of `var`.
- **Performance**: HTML should not reload for each action; use DOM manipulation and updates to values directly.

## Setup

1. **Node.js Installation**: Install Node.js for server-side JavaScript execution.
2. **Editor Configuration**: Configure your editor to follow semistandard coding style.
3. **Browser Testing**: Ensure all scripts are tested in Chrome browser (version 57.0 or later).

## Tasks

### Task 0: Color Me
Write a JavaScript script that updates the text color of the header element to red (#FF0000):

- Use `document.querySelector` to select the HTML tag.
- Test with provided `0-main.html`.

### Task 1: Click and Turn Red
Write a JavaScript script that updates the text color of the header element to red (#FF0000) when the user clicks on the tag with id `red_header`:

- Test with provided `1-main.html`.

### Task 2: Add `.red` Class
Write a JavaScript script that adds the class `red` to the header element when the user clicks on the tag with id `red_header`:

- Test with provided `2-main.html`.

### Task 3: Toggle Classes
Write a JavaScript script that toggles the class of the header element when the user clicks on the tag with id `toggle_header`:

- The header element must always have one class: `red` or `green`, never both, and never empty.
- Test with provided `3-main.html`.

### Task 4: List of Elements
Write a JavaScript script that adds a `li` element to a list when the user clicks on the element with id `add_item`:

- The new element must be: `<li>Item</li>`
- The new element must be added to the `ul` element with class `my_list`.
- Test with provided `4-main.html`.

### Task 5: Change the Text
Write a JavaScript script that updates the text of the header element to `New Header!!!` when the user clicks on the element with id `update_header`:

- Test with provided `5-main.html`.

### Task 6: Star Wars Character
Write a JavaScript script that fetches the character name from this URL: `https://swapi-api.hbtn.io/api/people/5/?format=json`

- The name must be displayed in the HTML tag with id `character`.
- Use the Fetch API.
- Test with provided `6-main.html`.

### Task 7: Star Wars Movies
Write a JavaScript script that fetches and lists the title for all movies by using this URL: `https://swapi-api.hbtn.io/api/films/?format=json`

- All movie titles must be listed in the HTML `ul` element with id `list_movies`.
- Use the Fetch API.
- Test with provided `7-main.html`.

### Task 8: Say Hello!
Write a JavaScript script that fetches from `https://hellosalut.stefanbohacek.dev/?lang=fr` and displays the value of `hello` from that fetch in the HTML element with id `hello`.

- The translation of “hello” must be displayed in the HTML element with id `hello`.
- Your script must work when it is imported from the `<head>` tag.
- Test with provided `8-main.html`.

## Resources

- [What is JavaScript?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Introduction)
- [Introduction to the DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction)
- [Document Interface](https://developer.mozilla.org/en-US/docs/Web/API/Document)
- [Element Class](https://developer.mozilla.org/en-US/docs/Web/API/Element)
- [Locating DOM elements using selectors](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector)
- [CSS Selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors)
- [CSS Diner: Play with Selectors](https://flukeout.github.io/)
- [Client-side Web APIs](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs)
- [Introduction to web APIs](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Introduction)
- [Manipulating documents](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Manipulating_documents)
- [Fetching data from the server](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)
- [What went wrong? Troubleshooting JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_went_wrong)

## Further Instructions

- Ensure to handle errors or incorrect data types gracefully within scripts.
- Utilize modern JavaScript syntax and features such as template literals and arrow functions where appropriate.
- Focus on robustness and readability of your code to ensure that it is maintainable and scalable.

This project serves as an excellent opportunity to understand the power and flexibility provided by JavaScript for dynamic and interactive web applications.
```