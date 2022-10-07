document.onkeydown = (e) => {
    // The Enter/Return key
    if (e.key === "Enter") {
      document.activeElement.click();
    }
  };
  