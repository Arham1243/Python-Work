let imgs = document.querySelectorAll("img");
for (let i = 0; i < imgs.length; i++) {
  const img = imgs[i];
  console.log(img.src);
}

let titles = document.querySelectorAll(".design-box-con h3");
titles.forEach((title) => {
  console.log(title.textContent);
});

let titlesc = document.querySelectorAll(".design-detail-btn a");
titlesc.forEach((titlec) => {
  console.log(titlec.href);
});



