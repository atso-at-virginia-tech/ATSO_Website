function changeTab(tabName){
    let activeTabs = Array.from(document.getElementsByClassName('active-link'));

    activeTabs.forEach((tab) => {
        tab.classList = '';
    });

    let tabs = Array.from(document.getElementById('sidebar').children);

    tabs.forEach((tab) =>{
        if(tab.children[0].innerText === tabName){
            tab.children[0].classList.add('active-link');
        }
    });
}