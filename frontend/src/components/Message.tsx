import React from "react";
import { motion, AnimatePresence } from "framer-motion";

export interface IMessage {
  message: string | undefined;
  isSuccess: boolean;
}

type Props = {
  message: IMessage;
};

function Message({ message }: Props) {
  return (
    <AnimatePresence>
      {message.message && (
        <motion.div
          initial={{ opacity: 0, y: 100 }}
          animate={{ opacity: 1, y: 0 }}
          exit={{ opacity: 0, y: 100 }}
          transition={{ type: "tween", duration: 0.3 }}
        >
          <div
            className={
              "border p-2 w-full mt-5 rounded-sm " +
              (message.isSuccess
                ? "bg-green-50 text-green-500 border-green-300"
                : "bg-red-50 text-red-500 border-red-200")
            }
          >
            {message.message}
          </div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}

export default Message;
