# Advanced Scientific Calculator  

This Python-based GUI calculator provides a sleek and efficient interface for performing both **basic arithmetic** and **scientific computations**. Built using **Tkinter**, it offers features like a history of recent calculations, trigonometric functions, logarithms, and more.

---

## Key Features  

- **Dynamic Input Panel**:  
  A responsive display area to show your input and results.  

- **Interactive History Tracker**:  
  Automatically stores the last 5 calculations for quick reference.  

- **Comprehensive Button Layout**:  
  Includes standard numbers, arithmetic operations, and scientific functions.  

- **Error Handling**:  
  Prevents invalid operations (e.g., dividing by zero or logarithms of negative numbers).  

---

## How It Works  

### Interface Overview  

The calculator GUI is divided into three sections:  

1. **Display Screen**:  
   Shows the equation being input or the computed result.  

2. **History Panel**:  
   Displays the five most recent computations for quick reference.  

3. **Functional Buttons**:  
   Categorized for ease of use: basic arithmetic, trigonometric functions, and constants.

<table>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/2809085b-c64c-4cfd-827f-01660212562c" alt="Screenshot of Calculator 1" width="300"></td>
    <td><img src="https://github.com/user-attachments/assets/e2c25979-89c1-4828-9156-cfbab0036414" alt="Screenshot of Calculator 2" width="300"></td>
  </tr>
</table>

---

### Functional Overview  

| **Feature**           | **Buttons**              | **Details**                                                                 |
|------------------------|--------------------------|-----------------------------------------------------------------------------|
| **Clear Input**        | `AC`                    | Wipes the current input completely.                                        |
| **Delete Last Digit**  | `⌫`                     | Removes the last character of the input.                                   |
| **Basic Operations**   | `+`, `-`, `*`, `/`, `%` | Standard operations: addition, subtraction, multiplication, division, percentage. |
| **Trigonometry**       | `sin`, `cos`, `tan`     | Computes sine, cosine, and tangent (in radians).                           |
| **Factorial**          | `n!`                    | Calculates factorial for integers from 0 to 12.                            |
| **Power**              | `x²`                    | Squares the current input.                                                 |
| **Logarithms**         | `ln`                    | Computes the natural logarithm of a positive number.                       |
| **Constants**          | `π`, `e`                | Inserts the values of π (3.14159) or e (2.71828).                          |
| **Decimal Points**     | `.`                     | Adds a decimal point for fractional numbers.                               |
| **Evaluation**         | `=`                     | Evaluates the entered expression.                                          |
| **Recent Entries**     | `History`               | Displays the five most recent calculations.                                |

---

## Step-by-Step Instructions  

### Performing Basic Calculations  

1. Launch the calculator by running the script.  
2. Enter numbers using the **numeric buttons** and select operators like `+`, `-`, etc.  
3. Press `=` to view the result.  

**Example**:  
- Input: `8 + 4`  
- Result: `12`

---

### Advanced Operations  

For operations like trigonometry or logarithms:  

1. Enter the number.  
2. Select the desired function (e.g., `sin`, `ln`).  
3. The result will be displayed instantly.  

**Example**:  
- Input: `1.5708` (approximately π/2) and select `sin`.  
- Result: `1.0`.

---

### Viewing History  

1. Press the `History` button to access past computations.  
2. The last five results are shown, numbered for clarity.  

**Example History**:  

<table>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/2b3ee0ea-2665-499f-8667-15aae920c796" alt="Screenshot of Calculator History 1" width="300"></td>
    <td><img src="https://github.com/user-attachments/assets/9ab08469-74eb-44ce-b4f0-a5a482325337" alt="Screenshot of Calculator History 2" width="300"></td>
  </tr>
</table>

---

## Error Handling  

- **Invalid Inputs**:  
  If you enter an invalid equation or perform unsupported operations (e.g., `ln(-1)`), the display shows `Error`.  

- **Factorial Limits**:  
  Factorials are calculated for integers up to 12. Larger values prompt a warning.

---

## Highlights of Design  

1. **Modern Aesthetics**:  
   - Clean and colorful button layout for quick navigation.  

2. **Interactive Feedback**:  
   - Real-time updates to the display as buttons are pressed.  

3. **Compact History Feature**:  
   - Keeps a concise record of past results for quick reference.  

4. **Optimized Performance**:  
   - Prevents overly long inputs or invalid expressions to ensure smooth functionality.  

---

## Sample Execution Flow  

### Example 1: Arithmetic Operation  

- **Input**: `5 * 7`  
- **Steps**:  
   - Enter `5`.  
   - Press `*`.  
   - Enter `7` and press `=`.  
- **Output**: `35`.

### Example 2: Advanced Function  

- **Input**: `ln(e)`  
- **Steps**:  
   - Press `e` to insert Euler's number.  
   - Select `ln`.  
- **Output**: `1.0`.  

---

## Running the Application  

To use this calculator:  

1. Clone or download this repository.  
2. Ensure Python 3.x is installed on your system.  
3. Install **Tkinter** (usually pre-installed with Python).  
4. Run the script using the command:



Thank You!!
