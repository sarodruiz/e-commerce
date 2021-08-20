document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.add-btn').forEach(btn => {
        btn.onclick = () => {
            add_to_cart(btn.dataset.id);
        }
    });
});

function add_to_cart(item_id) {
    item_size = document.querySelector(`#size-${item_id}`).value;

    fetch('/add-to-cart/', {
        method: 'POST',
        body: JSON.stringify({
            id: item_id,
            size: item_size
        })
    })
    .then(response => response.json())
    .then(data => console.log(data));
}