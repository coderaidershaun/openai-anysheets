import { useState, useCallback } from "react";
import { IMessage } from "./Message";
import FileDownload from "js-file-download";
import Message from "./Message";
import SubmitButton from "./SubmitButton";
import axios from "axios";

// Sets the default prompt and placeholder
const defaultPrompt =
  "/excel has the latest crypto price data from Binance.\
 There is a cell C1 which is labelled pink elephants with pink text.";

function Controller() {
  const [promptType, setPromptType] = useState<string | undefined>(undefined);
  const [prompt, setPrompt] = useState<string | undefined>(undefined);
  const [bgColors, setBgColors] = useState("from-gray-700 to-gray-800");
  const [isDisabled, setIsDisabled] = useState(true);
  const [isLoading, setIsLoading] = useState(false);
  const [fileName, setFileName] = useState("savedfile.xlsx");
  const [message, setMessage] = useState<IMessage>({
    message: undefined,
    isSuccess: false,
  });

  // Handle storing prompt values
  const updatePrompt = useCallback(
    (e: any) => {
      let val = e.target.value;

      // Prompt type
      const isExcel = val.includes("/excel");
      const isPdf = val.includes("/pdf");
      const isWord = val.includes("/word");
      const isPowerpoint = val.includes("/powerpoint");

      if (isExcel && !promptType) {
        setPromptType("/excel");
        setBgColors("from-green-500 to-green-700");
        setFileName("savedfile.xlsx");
      }

      if (isPdf && !promptType) {
        setPromptType("/pdf");
        setBgColors("from-pink-500 to-pink-700");
        setFileName("savedfile.pdf");
      }

      if (isWord && !promptType) {
        setPromptType("/word");
        setBgColors("from-blue-500 to-blue-700");
        setFileName("savedfile.docx");
      }

      if (isPowerpoint && !promptType) {
        setPromptType("/powerpoint");
        setBgColors("from-red-500 to-red-700");
        setFileName("savedfile.pptx");
      }

      if (!isExcel && !isPdf && !isWord && !isPowerpoint) {
        setIsDisabled(true);
        setPromptType(undefined);
        setBgColors("from-gray-700 to-gray-800");
      } else {
        setIsDisabled(false);
      }

      setPrompt(val);
    },
    [prompt, setPrompt]
  );

  const handleSubmit = async (e: any) => {
    e.preventDefault();

    // Initialize
    setIsLoading(true);
    setMessage({
      message: undefined,
      isSuccess: false,
    });

    // Construct request
    if (prompt && promptType) {
      const body = {
        prompt,
        promptType,
      };

      // Send script request
      await axios
        .post("http://localhost:8000/build-script/", body, {
          withCredentials: true,
        })
        .then(async (res) => {
          if (res.status == 200) {
            // Send execute script request
            await axios
              .get("http://localhost:8000/execute-query/" + fileName, {
                responseType: "blob",
              })
              .then((res) => {
                if (res.status == 200) {
                  // Create blob link to download
                  FileDownload(res.data, fileName);
                  setMessage({
                    message: "Your file is ready",
                    isSuccess: true,
                  });
                }
              })
              .catch((err) => {
                setMessage({
                  message: "There was an issue building the file",
                  isSuccess: false,
                });
                console.error(err.message);
              });
          }
        })
        .catch((err) => {
          setMessage({
            message: "There was an issue creating the script",
            isSuccess: false,
          });
          console.error(err.message);
        });
    }

    // Cleanup
    setIsLoading(false);
  };

  return (
    <div className={"w-screen h-screen bg-gradient-to-br " + bgColors}>
      <div className="flex flex-col h-full w-full justify-center items-center">
        <h2 className="text-5xl">Create Anything</h2>
        <h3 className="mt-1 font-light text-lg">
          Start your prompt with /excel or /pdf or /word has ...
        </h3>
        <form
          onSubmit={handleSubmit}
          className="flex flex-col items-center justify-center w-full mt-2"
        >
          <div className="relative mx-auto w-11/12 md:w-2/3 lg:w-7/12">
            <textarea
              value={prompt}
              onChange={updatePrompt}
              placeholder={defaultPrompt}
              maxLength={300}
              className="w-full transition-all duration-200 shadow-xl border-2 focus:border-sky-500 focus:shadow-inner bg-white text-gray-500 px-5 py-5 outline-0 appearance-none text-lg rounded mt-5"
            />
            <div className="absolute top-2 left-8 text-lg px-2 bg-sky-500 rounded">
              {promptType}
            </div>
          </div>
          <SubmitButton
            isDisabled={isDisabled || isLoading}
            isLoading={isLoading}
          />
        </form>
        <Message message={message} />
      </div>
    </div>
  );
}

export default Controller;
