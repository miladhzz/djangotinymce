function FileBrowserPopup(callback, value, type) {
    var fbURL = '/admin/filebrowser/browse/?pop=5';
    fbURL = fbURL + "&type=" + type.filetype;
    if(value)
        fbURL += '&input=';
    const instanceApi = tinyMCE.activeEditor.windowManager.openUrl({
        title: 'Filebrowser image/media/file picker',
        url: fbURL,
        width: 850,
        height: 500,
        onMessage: function(dialogApi, details) {
            callback(details.content);
            instanceApi.close();
        }
    });
    return false;
}

tinymce.init({
  selector: 'textarea#id_content',
  menubar: 'view',
  toolbar: 'undo redo | bold italic underline strikethrough | fontsizeselect formatselect | alignleft aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor backcolor casechange permanentpen formatpainter removeformat | charmap emoticons | fullscreen | insertfile image media link codesample | a11ycheck ltr rtl ',
  plugins: 'paste importcss searchreplace autolink autosave save directionality code visualblocks visualchars fullscreen image link media codesample table charmap hr toc insertdatetime advlist lists wordcount imagetools textpattern noneditable charmap quickbars emoticons',
  image_caption: true,
  image_advtab: true,
  file_picker_callback: FileBrowserPopup,
  content_style: 'body { font-family:Helvetica,Arial,sans-serif; font-size:14px }'
});
