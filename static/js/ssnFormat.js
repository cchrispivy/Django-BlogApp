function ssnFormatter() {
	const inputField = document.getElementById("ssn");
	const formatedValue = formatSSN(inputField.value);
	inputField.value = formattedInputValue;
}

function formatSSN(value) {
  if (!value) return value;
  const ssn = value.replace(/[^\d]/g, '');
  const ssnLength = ssn.length;
  if (ssnLength < 4) return ssn;

  if (ssnLength < 6) {
    return `${ssn.slice(0, 3)}-${ssn.slice(3)}`;
  }

  return `${ssn.slice(0, 3)}-${ssn.slice(3, 5)}-${ssn.slice(5, 8)}`;
}

