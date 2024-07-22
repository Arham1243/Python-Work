// ---------------------------------------User Management---------------------------------------
Route::get('/users-listing', [AdminDashController::class, 'usersListing'])->name('admin.usersListing');
Route::get('/view-user/{id}', [AdminDashController::class, 'editUser'])->name('admin.editUser');
Route::get('/suspend-user/{id}', [AdminDashController::class, 'suspendUser'])->name('admin.suspendUser');
Route::get('/delete-user/{id}', [AdminDashController::class, 'deleteUser'])->name('admin.deleteUser');
// ---------------------------------------User Management---------------------------------------