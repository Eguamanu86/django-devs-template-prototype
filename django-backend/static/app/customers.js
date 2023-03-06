const tbody = document.querySelector("#id-customers-table > tbody")

tbody.addEventListener('click', async (event) => {
  event.preventDefault();
  // capturamos la accion-depositar monto
  if (event.target.closest('a[rel="accion-eliminar"]')) {
    const customerId = event.target.dataset.id
    if (confirm('Esta seguro de eliminar el registro de cliente')) {

      try {

        const options = {
          method: 'DELETE',
          credentials: 'same-origin',
          headers: {
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
            'X-CSRFToken': Cookies.get('csrftoken')
          }
        }

        const response = await fetch(`/customers/delete/${customerId}`, options)
        if (!response.ok) {
          throw response
        }
        const data = await response.json()
        console.log(data)
        event.target.closest('tr').remove()

      } catch (error) {
        let message;
        if (error instanceof Response) {
          responseError = await error.json()
          message = responseError.errors.join(',')
        } else {
          message = error.message ?? error
        }

      }

    }
  }

})
