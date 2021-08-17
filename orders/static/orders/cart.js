document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.remove-btn').forEach(btn => {
        btn.onclick = event => {
            remove_from_cart(1);
        }
    });
});

function remove_from_cart(item_id) {
    //item_size = document.querySelector(`#size-${item_id}`).value;

    fetch('/remove-from-cart', {
        method: 'POST',
        body: JSON.stringify({
            id: item_id
            //size: item_size
        })
    })
    .then(response => response.json())
    .then(data => location.reload());
}