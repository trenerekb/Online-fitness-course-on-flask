// UPLOAD FUNCTION
function upload(selector, options={}) {
   let files = []
   const images_report = document.querySelector('.images-report')
   const input = document.querySelector(selector)
   const open = document.createElement('button')
   if (options.multi) {
      input.setAttribute('multiple', true)
   }
   const triggerInput = () => input.click()
   const changeHandler = () => {
      if (!event.target.files.length) {
         return
      }
      files = Array.from(event.target.files)
//      images_report.innerHTML = ''
      files.forEach(file => {
         if (!file.type.match('image')) {
            return
         }
         const reader = new FileReader()
         reader.onload = ev => {
            const img = document.createElement('img')
            images_report.insertAdjacentHTML('afterbegin', `<div class="img-report">
            <div class="preview-remove" data-name="${file.name}">&times;</div>
            <img src="${reader.result}" alt="${file.name}"/></div>`)
         }
         reader.readAsDataURL(file)
      })
   }
   const removeHandler = event => {
      if (!event.target.dataset.name) {
         return
      }
      const {name} = event.target.dataset
      files = files.filter(file => file.name !== name)
      const block = images_report.querySelector(`[data-name="${name}"]`).closest('.img-report')
      block.remove()
   }
   open.addEventListener('click', triggerInput)
   input.addEventListener('change', changeHandler)
   images_report.addEventListener('click', removeHandler )
}
upload('#file', {multi: true})