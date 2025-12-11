'use client';
import { useEffect, useState } from "react";
import Link from "next/link";
export default function Home() {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [err, setErr] = useState("");
  const [updatingId, setUpdatingId] = useState(null);
  const [deletingId, setDeletingId] = useState(null);

  useEffect(() => {
    const run = async () => {
      try {
        const res = await fetch("http://localhost:5000/", { method: "GET" });
        if (!res.ok) {
          const text = await res.text();
          throw new Error(`HTTP ${res.status}: ${text}`);
        }
        const data = await res.json();
        setTasks(Array.isArray(data) ? data : []);
      } catch (e) {
        console.error(e);
        setErr(e.message || "Failed to fetch tasks");
      } finally {
        setLoading(false);
      }
    };
    run();
  }, []);

  // Toggle status: Pending -> Completed, Completed -> Pending
  const toggleStatus = async (id, currentStatus) => {
    const nextStatus =
      String(currentStatus || "").trim().toLowerCase() === "pending"
        ? "Completed"
        : "Pending";

    // Optimistic update
    setUpdatingId(id);
    const prevTasks = tasks;
    setTasks((prev) =>
      prev.map((t) => (t[0] === id ? [t[0], t[1], t[2], nextStatus, t[4]] : t))
    );

    try {
      const res = await fetch(`http://localhost:5000/update/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ status: nextStatus }),
      });
      if (!res.ok) {
        const text = await res.text();
        throw new Error(`HTTP ${res.status}: ${text}`);
      }
    } catch (e) {
      console.error(e);
      setErr(e.message || "Failed to update");
      setTasks(prevTasks); // rollback on error
    } finally {
      setUpdatingId(null);
    }
  };

  // Delete task
  const deleteTask = async (id) => {
    setDeletingId(id);
    const prevTasks = tasks;
    // Optimistic remove
    setTasks((prev) => prev.filter((t) => t[0] !== id));

    try {
      const res = await fetch(`http://localhost:5000/del/${id}`, {
        method: "DELETE",
      });
      if (!res.ok) {
        const text = await res.text();
        throw new Error(`HTTP ${res.status}: ${text}`);
      }
    } catch (e) {
      console.error(e);
      setErr(e.message || "Failed to delete");
      setTasks(prevTasks);
    } finally {
      setDeletingId(null);
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100">
      <div className="w-full max-w-2xl">
      <div className="flex w-full justify-between items-center gap-4 mb-8">
        <h1 className="text-5xl font-bold  text-left">TODO</h1>

        <Link

            href="/add"
            className="ml-2 px-4 py-2 font-medium rounded-lg p-6">  <p className="text-5xl font-bold text-right">Add</p> </Link>
         </div>

        <div className="bg-white shadow-md rounded-lg p-6">
          {loading && <p className="text-gray-500 text-center">Loading tasks...</p>}
          {err && <p className="text-red-600 text-center mb-4">{err}</p>}

          {!loading && !err && (
            <ul className="space-y-4">
              {tasks.length === 0 ? (
                <li className="text-center text-gray-500">No tasks found</li>
              ) : (
                tasks.map((task) => {
                  // task format: [id, title, description, status, created_at]
                  const [id, title, description, statusRaw, createdAtRaw] = task;
                  const status = String(statusRaw || "").trim();
                  const isPending = status.toLowerCase() === "pending";

                  const badgeClasses = isPending
                    ? "bg-orange-100 text-orange-700"
                    : "bg-green-100 text-green-700";

                  const buttonLabel = isPending ? "Done" : "Undone";
                  const buttonClasses = isPending
                    ? "bg-green-600 hover:bg-green-700"
                    : "bg-orange-600 hover:bg-orange-700";

                  return (
                    <li
                      key={id}
                      className="border border-gray-200 rounded-md p-4 hover:shadow-sm transition-shadow bg-white"
                    >
                      {/* Top row: title + status badge */}
                      <div className="flex items-start justify-between gap-4">
                        <p className="font-semibold text-lg">{title}</p>
                        <span
                          className={`inline-flex items-center px-2.5 py-1 rounded text-xs font-medium ${badgeClasses}`}
                          title={`Status: ${status}`}
                        >
                          {status}
                        </span>
                      </div>

                      {/* Description */}
                      {description && (
                        <p className="text-gray-600 mt-1">{description}</p>
                      )}

                      {/* Bottom row: date (left) + buttons (right) */}
                      <div className="mt-2 flex items-center justify-between">
                        {/* Date (small) */}
                        {createdAtRaw && (
                          <p className="text-sm text-gray-400">{createdAtRaw}</p>
                        )}

                        {/* Action buttons */}
                        <div className="flex items-center gap-2">
                          <button
                            onClick={() => toggleStatus(id, status)}
                            disabled={updatingId === id}
                            className={`px-3 py-1 text-sm text-white rounded transition-colors ${
                              buttonClasses
                            } ${
                              updatingId === id
                                ? "opacity-60 cursor-not-allowed"
                                : ""
                            }`}
                            aria-label={`Mark as ${
                              isPending ? "Completed" : "Pending"
                            }`}
                            title={`Mark as ${
                              isPending ? "Completed" : "Pending"
                            }`}
                          >
                            {buttonLabel}
                          </button>

                          <button
                            onClick={() => deleteTask(id)}
                            disabled={deletingId === id}
                            className={`px-3 py-1 text-sm text-white rounded transition-colors bg-red-600 hover:bg-red-700 ${
                              deletingId === id
                                ? "opacity-60 cursor-not-allowed"
                                : ""
                            }`}
                            aria-label="Delete task"
                            title="Delete task"
                          >
                            Delete
                          </button>
                        </div>
                      </div>
                    </li>
                  );
                })
              )}
            </ul>
          )}
        </div>
      </div>
    </div>

  );
}
