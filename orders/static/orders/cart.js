document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.remove-btn').forEach(btn => {
        btn.onclick = event => {
            remove_from_cart(btn.dataset.id);
        }
    });
});

function remove_from_cart(item_id) {
    fetch('/remove-from-cart/', {
        method: 'POST',
        body: JSON.stringify({
            id: item_id
        })
    })
    .then(response => response.json())
    .then(data => location.reload());
}