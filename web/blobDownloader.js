function download(pdfUrl) {
        fetch(pdfUrl).then(resp => resp.arrayBuffer()).then(resp => {

            // set the blog type to final pdf
            const file = new Blob([resp], {type: 'application/pdf'});

            // process to auto download it
            const fileURL = URL.createObjectURL(file);
            const link = document.createElement('a');
            link.href = fileURL;
            link.download = "FileName" + new Date() + ".pdf";
            link.click();
        });
    }

download("blob:url")
