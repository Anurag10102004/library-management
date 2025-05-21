document.getElementById('bookForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const title = document.getElementById('title').value;
    const author = document.getElementById('author').value;
    const year = document.getElementById('year').value;

    const table = document.getElementById('bookTable').getElementsByTagName('tbody')[0];
    const newRow = table.insertRow();

    const titleCell = newRow.insertCell(0);
    const authorCell = newRow.insertCell(1);
    const yearCell = newRow.insertCell(2);

    titleCell.textContent = title;
    authorCell.textContent = author;
    yearCell.textContent = year;

    // Clear the form
    document.getElementById('bookForm').reset();
});
