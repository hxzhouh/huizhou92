function detectAdBlocker() {
    const adBlockTest = document.createElement('div');
    adBlockTest.innerHTML = '&nbsp;';
    adBlockTest.className = 'ad ads adbadge doubleclick BannerAd adsbox ad-placeholder ad-placement';
    document.body.appendChild(adBlockTest);
    window.setTimeout(() => {
      if (adBlockTest.offsetHeight === 0) {
        document.getElementById('adblock-warning').style.display = 'block';
        console.log('Ad-blocker detected.');
      } else {
        console.log('No ad-blocker detected.');
      }
      adBlockTest.remove();
    }, 100);
  }
  
  window.addEventListener('load', detectAdBlocker);