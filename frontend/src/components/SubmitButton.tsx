import React from "react";

type Props = {
  isDisabled?: boolean;
};

function SubmitButton({ isDisabled }: Props) {
  return (
    <button
      type="submit"
      className={
        "appearance-none outline-0 focus:outline-0 shadow-lg border rounded mt-7 " +
        (isDisabled
          ? "bg-gray-200 text-gray-500 shadow-none"
          : "transition-all duration-200 border-sky-600 focus:shadow-inner hover:shadow-inner focus:bg-sky-500 bg-sky-500 hover:bg-sky-600 text-white")
      }
    >
      CREATE
    </button>
  );
}

export default SubmitButton;
