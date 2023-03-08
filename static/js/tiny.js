// console.log('welcome shubhanshu bhai ji ..............')

// document.addEventListener("DOMContentLoaded", function(event) {
//     let sc = document.createElement('script');
//     sc.setAttribute('src', "https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js")
//     document.head.appendChild(sc);

//     // <style>
//     // #id_content{
//     //     height : 80vh;
//     // }
//     // </style>
//     sc.onload = () =>
//         tinymce.init({
//             selector: '#id_content',
//             plugins: [
//                 'advlist autolink link image lists charmap print preview hr anchor pagebreak',
//                 'searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking',
//                 'table emoticons template paste help', 'image code',
//             ],
//             toolbar1: 'undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | ' +
//                 'bullist numlist outdent indent | link image | print preview media fullpage | ' +
//                 'forecolor backcolor emoticons | help',
//             // toolbar2:'undo redo | link image | code',
//             // enable title field in the Image dialog
//             image_title: true,
//             // enable automatic uploads of images represented by blob or data URIs
//             automatic_uploads: true,
//             // add custom filepicker only to Image dialog
//             file_picker_types: 'image',
//             file_picker_callback: function(cb, value, meta) {
//                 var input = document.createElement('input');
//                 input.setAttribute('type', 'file');
//                 input.setAttribute('accept', 'image/*');

//                 input.onchange = function() {
//                     var file = this.files[0];
//                     var reader = new FileReader();

//                     reader.onload = function() {
//                         var id = 'blobid' + (new Date()).getTime();
//                         var blobCache = tinymce.activeEditor.editorUpload.blobCache;
//                         var base64 = reader.result.split(',')[1];
//                         var blobInfo = blobCache.create(id, file, base64);
//                         blobCache.add(blobInfo);

//                         // call the callback and populate the Title field with the file name
//                         cb(blobInfo.blobUri(), { title: file.name });
//                     };
//                     reader.readAsDataURL(file);
//                 };

//                 input.click();
//             },

//             menu: {
//                 favs: { title: 'My Favorites', items: 'code visualaid | searchreplace | emoticons' }
//             },
//             menubar: 'favs file edit view insert format tools table help',

//             content_css: 'css/content.css'
//         });
// });





var script = document.createElement('script');
script.type = 'text/javascript';
script.src = "https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js";
document.head.appendChild(script);

script.onload = function() {
    tinymce.init({
        selector: "#id_content",
        height: 656,
        plugins: [
            'advlist autolink link image lists charmap print preview hr anchor pagebreak',
            'searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking', 'image imagetools',
            'table emoticons template paste help'
        ],
        toolbar: 'undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | ' +
            'bullist numlist outdent indent | link image | print preview media fullpage | ' +
            'forecolor backcolor emoticons | help',
        menu: {
            favs: { title: 'My Favorites', items: 'code visualaid | searchreplace | emoticons' }
        },
        menubar: 'favs file edit view insert format tools table help',
        content_css: 'css/content.css'
    });
}